import axios from "axios";
import React, { useEffect, useState, useContext } from "react";
import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import Spiner from "../Spiner/Spiner";
import { FavContext } from "../../Context/FavContext";
import { Link } from "react-router-dom";
import { FaStar } from "react-icons/fa";

export default function Videodetail() {
  const token = localStorage.getItem("usertoken");
  const [favoritedVideos, setFavoritedVideos] = useState([]);
  const [details, setDetails] = useState(null);
  const parms = useParams();

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
      const newFavorites = [...favoritedVideos, videoName];
      setFavoritedVideos(newFavorites);
      localStorage.setItem("favoriteVideos", JSON.stringify(newFavorites));
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

  function getVideoDetail(title) {
    return axios.get(
      `https://youssifallam.pythonanywhere.com/api/v1/Videos/Get-Video-Details/?video_title=${title}`,
      {
        headers: {
          Authorization:
            "Bearer " +
            token,
        },
      }
    );
  }

  let { isError, isLoading, data } = useQuery("videodetail", () =>
    getVideoDetail(parms.title)
  );

  console.log(parms);
  console.log("data video detail", data?.data.data.video);
  console.log("error video detail", isError);
  console.log("loading video detail", isLoading);

  function getRelatedVideos() {
    return axios.get(
      "https://youssifallam.pythonanywhere.com/api/v1/Videos/Get_All_Videos/"
    );
  }

  let { data: relatedVideosData } = useQuery(
    "getrelvideosApi",
    getRelatedVideos
  );

  useEffect(() => {
    if (data && data.data.data.video) {
      setDetails(data.data.data.video);
    }
  }, [data]);

  const loadVideoDetails = (title) => {
    const video = relatedVideosData.data.data.videos.find(
      (video) => video.title === title
    );
    setDetails(video);
  };

  return (
    <>
      {isLoading ? (
        <Spiner />
      ) : (
        <div className="container">
          {details ? (
            <div className="row py-2">
              <div className="col-md-8">
                <div className="video contentVideoDetail ms-5 p-4">
                  <video
                    className="cursor-pointer "
                    src={details.video_file}
                    controls
                    width="50"
                  />
                  <div className="d-flex justify-content-between ">
                    <div>
                      <h2>{details.title}</h2>
                      <h3>{details.description}</h3>
                    </div>
                    {isVideoFavorited(details.title) ? (
                      <FaStar
                        className="fav"
                        onClick={() => removeVideo(details.title)}
                        style={{
                          color: "#FFD43B",
                          cursor: "pointer",
                        }}
                      />
                    ) : (
                      <FaStar
                        onClick={() => addVideoToFav(details.title)}
                        style={{
                          color: isVideoFavorited(details.title)
                            ? "#FFD43B"
                            : "#808080",
                          cursor: "pointer",
                        }}
                      />
                    )}
                  </div>
                </div>
              </div>
              <div className="col-md-4 pe-5">
                <div className="row">
                  {relatedVideosData?.data?.data?.videos &&
                    relatedVideosData.data.data.videos.map((element) => {
                      const isMatch = element.title === details.title;
                      const relatedVideoStyle = {
                        border: isMatch
                          ? "2px solid #2dbddd"
                          : "2px solid transparent",
                      };

                      return (
                        <div key={element.id} className="col-md-12 m-3 ">
                          <div
                            className="videos w-100"
                            style={relatedVideoStyle}
                            onClick={() => loadVideoDetails(element.title)}
                          >
                            <img
                              src={element.thumbnail}
                              alt="video thumbnail"
                              width="100%"
                              height="auto"
                            />
                            <h4 className="text-center">{element.title}</h4>
                          </div>
                          {/* <div className="">
                            {isVideoFavorited(element.title) ? (
                              <FaStar
                                className="fav"
                                onClick={() => removeVideo(element.title)}
                                style={{
                                  color: "#FFD43B",
                                  cursor: "pointer",
                                }}
                              />
                            ) : (
                              <FaStar
                                onClick={() => addVideoToFav(element.title)}
                                style={{
                                  color: "#FFD43B",
                                  cursor: "pointer",
                                }}
                              />
                            )}
                          </div> */}
                        </div>
                      );
                    })}
                </div>
              </div>
            </div>
          ) : (
            ""
          )}
        </div>
      )}
    </>
  );
}

