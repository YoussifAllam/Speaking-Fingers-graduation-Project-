import React, { useEffect, useState, useContext } from "react";
import axios from "axios";
import Spiner from "../Spiner/Spiner";
import { useQuery } from "react-query";
import { Link } from "react-router-dom";
import { FaStar as StarFilled, FaStar as StarOutline } from "react-icons/fa";
import { FavContext } from "../../Context/FavContext";

export default function Favvideos() {
  const token = localStorage.getItem("usertoken");
  const [favoritedVideos, setFavoritedVideos] = useState([]);
  useEffect(() => {
    const storedFavorites = JSON.parse(localStorage.getItem("favoriteVideos"));
    if (storedFavorites) {
      setFavoritedVideos(storedFavorites);
    }
  }, []);

  const { AddToFav, deleteFavVideo } = useContext(FavContext);

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

  async function removeVideo(videoName) {
    try {
      let response = await deleteFavVideo(videoName);
      console.log("videos deleted", response);
      if (response.status === 204) {
        setFavoritedVideos((prevVideos) =>
          prevVideos.filter((video) => video !== videoName)
        );
        refetch();
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
      "https://youssifallam.pythonanywhere.com/api/v1/Videos/Get-user-favorites-videos/",
      {
        headers: {
          Authorization:
            "Bearer " +
            token,
        },
      }
    );
  }

  let { data, isLoading, refetch, isError } = useQuery(
    "getvideosApi",
    getvideos
  );

  return (
    <>
      {isLoading ? (
        <Spiner />
      ) : (
        <div className="container conta3">
          <h4 className="ms-5 mt-3 mb-2 fw-bold fav">Favorite Videos</h4>
          <div className="row">
            {Array.isArray(data?.data?.data) &&
              data?.data?.data.map((element) => (
                <div key={element.id} className="col-md-4 ps-5">
                  <Link to={`/Videodetail/${element.video.title}`}>
                    <div className="videos">
                      <video
                        className="cursor-pointer"
                        src={element.video.video_file}
                        controls
                        width="400"
                        height="300"
                      />
                    </div>
                  </Link>
                  <div className="d-flex justify-content-between">
                    <h4>{element.video.title}</h4>
                    {isVideoFavorited(element.video.title) ? (
                      <StarFilled
                        className="fav"
                        onClick={() => removeVideo(element.video.title)}
                        style={{ color: "#FFD43B", cursor: "pointer" }}
                      />
                    ) : (
                      <StarOutline
                        onClick={() => addVideoToFav(element.video.title)}
                        style={{ color: "#FFD43B", cursor: "pointer" }}
                      />
                    )}
                  </div>
                </div>
              ))}
          </div>
        </div>
      )}
    </>
  );
}
