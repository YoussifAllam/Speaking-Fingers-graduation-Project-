import React, { useContext, useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { FavContext } from "../../Context/FavContext";
import { FaStar } from "react-icons/fa";
import { useQuery } from "react-query";
import Spiner from "../Spiner/Spiner";

import style from "./Videos.module.css";
export default function Videos() {
  const [favoritedVideos, setFavoritedVideos] = useState([]);
  useEffect(() => {
    const storedFavorites = JSON.parse(localStorage.getItem("favoriteVideos"));
    if (storedFavorites) {
      setFavoritedVideos(storedFavorites);
    }
  }, []);
  const AddToFav = useContext(FavContext).AddToFav;
  const deleteFavVideo = useContext(FavContext).deleteFavVideo;

  async function addVideoToFav(videoName) {
    let response = await AddToFav(videoName);
    console.log("video added", response.data);
    if (response.data.message === "Video favorited successfully.") {
      const newFavrites = [...favoritedVideos, videoName];
      setFavoritedVideos(newFavrites);
      localStorage.setItem("favoriteVideos", JSON.stringify(newFavrites));
    } else {
      alert("video is already in fav");
    }
  }

  async function removevideo(videoName) {
    try {
      let response = await deleteFavVideo(videoName);
      console.log("videos deleted", response);
      if (response.status === 204) {
        setFavoritedVideos((prevVideos) =>
          prevVideos.filter((video) => video !== videoName)
        );
        localStorage.setItem(
          "favoriteVideos",
          JSON.stringify(favoritedVideos.filter((video) => video !== videoName))
        );
      } else {
        alert("Failed to remove video from favorites.");
      }
    } catch (error) {
      console.error("Error removing video:", error);
      alert("An error occurred while removing video from favorites.");
    }
  }

  function isVideoFavorited(videoName) {
    return favoritedVideos.includes(videoName);
  }

  function getvideos() {
    return axios.get(
      "https://youssifallam.pythonanywhere.com/api/v1/Videos/Get_All_Videos/"
    );
  }

  let { data, isLoading, isFetching, refetch, isError } = useQuery(
    "getvideosApi",
    getvideos
  );

  return (
    <>
      {isLoading ? (
        <Spiner />
      ) : (
        <div className={style.bodyy}>
          <div className="container conta3">
            <h4 className="ps-5 fav fw-bold "> Videos to learn Sign Language</h4>
            <div className="row">
              {data?.data?.data?.videos &&
                data.data.data.videos.map((element) => {
                  return (
                    <div
                      key={element.id}
                      className={` ${style.vid} col-md-4  `}
                    >
                      <Link to={`/Videodetail/${element.title}`}>
                        <video
                          className="cursor-pointer videos"
                          src={element.video_file}
                          controls
                          width="200 px"
                          height="300"
                        />
                      </Link>
                      <div>
                        <div className="d-flex justify-content-between">
                          <Link to={`/Videodetail/${element.title}`}>
                            <h4>{element.title}</h4>
                          </Link>
                          <FaStar
                            className="cursor-pointer"
                            onClick={() => {
                              if (isVideoFavorited(element.title)) {
                                removevideo(element.title);
                              } else {
                                addVideoToFav(element.title);
                              }
                            }}
                            style={{
                              color: isVideoFavorited(element.title)
                                ? "#FFD43B"
                                : "#808080",
                            }}
                          />
                        </div>
                      </div>
                    </div>
                  );
                })}
            </div>
          </div>
        </div>
      )}
    </>
  );
}
