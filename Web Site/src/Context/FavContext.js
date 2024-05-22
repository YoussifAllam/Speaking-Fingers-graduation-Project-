// import axios from "axios";
// import { createContext } from "react";

// export let FavContext = createContext();

// export default function FavContextProvider(props) {
//   // اضافه الفيدوهات المفضله api
//   function AddToFav(videoName) {
//     let formData = new FormData();

//     formData.append("video_title", videoName);
//     return axios
//       .post(
//         `https://youssifallam.pythonanywhere.com/api/v1/Videos/add-fav-video-to-user/`,
//         formData,
//         {
//           headers: {
//             Authorization:
//               "Bearer " +
//               "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1ODg1MDM3LCJpYXQiOjE3MTQ1ODkwMzcsImp0aSI6IjBmYzBlOWNlZjM5OTQ2YTc4M2U3M2YwMTJhYzViNjM5IiwidXNlcl9pZCI6MTkyfQ.ll-5xeZO6AWHXa6ivmx9z5xoNm9DDANybC0zg-WHg7w",
//           },
//         }
//       )
//       .then((Response) => Response)
//       .catch((Error) => Error);
//   }
//   // get fav videos api
//   function getUserFavVideos() {
//     return axios
//       .get(
//         "https://youssifallam.pythonanywhere.com/api/v1/Videos/Get-user-favorites-videos/",
//         {
//           headers: {
//             Authorization:
//               "Bearer " +
//               "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1ODg1MDM3LCJpYXQiOjE3MTQ1ODkwMzcsImp0aSI6IjBmYzBlOWNlZjM5OTQ2YTc4M2U3M2YwMTJhYzViNjM5IiwidXNlcl9pZCI6MTkyfQ.ll-5xeZO6AWHXa6ivmx9z5xoNm9DDANybC0zg-WHg7w",
//           },
//         }
//       )
//       .then((Response) => Response)
//       .catch((Error) => Error);
//   }
//   function deleteFavVideo(videoName) {
//     // let formData = new FormData();

//     // formData.append("video_title", videoName);
//     return axios
//       .delete(
//         "https://youssifallam.pythonanywhere.com/api/v1/Videos/remove-favorite-video/",
//         // formData,
//         {
//           headers: {
//             Authorization:
//               "Bearer " +
//               "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1ODg1MDM3LCJpYXQiOjE3MTQ1ODkwMzcsImp0aSI6IjBmYzBlOWNlZjM5OTQ2YTc4M2U3M2YwMTJhYzViNjM5IiwidXNlcl9pZCI6MTkyfQ.ll-5xeZO6AWHXa6ivmx9z5xoNm9DDANybC0zg-WHg7w",
//           },
//           data: {
//             video_title: videoName,
//           },
//         }
//       )
//       .then((Response) => Response)
//       .catch((Error) => Error);
//   }
//   return (
//     <FavContext.Provider value={{ AddToFav, getUserFavVideos, deleteFavVideo }}>
//       {props.children}
//     </FavContext.Provider>
//   );
// }
import axios from "axios";
import { createContext } from "react";

export let FavContext = createContext();

export default function FavContextProvider(props) {
  const token = localStorage.getItem("usertoken");
  // اضافه الفيدوهات المفضله api
  function AddToFav(videoName) {
    let formData = new FormData();

    formData.append("video_title", videoName);
    return axios
      .post(
        'https://youssifallam.pythonanywhere.com/api/v1/Videos/add-fav-video-to-user/',
        formData,
        {
          headers: {
            Authorization: "Bearer " + token,
          },
        }
      )
      .then((Response) => Response)
      .catch((Error) => Error);
  }
  // get fav videos api
  function getUserFavVideos() {
    return axios
      .get(
        "https://youssifallam.pythonanywhere.com/api/v1/Videos/Get-user-favorites-videos/",
        {
          headers: {
            Authorization: "Bearer " + token,
          },
        }
      )
      .then((Response) => Response)
      .catch((Error) => Error);
  }
  function deleteFavVideo(videoName) {
    // let formData = new FormData();

    // formData.append("video_title", videoName);
    return axios
      .delete(
        "https://youssifallam.pythonanywhere.com/api/v1/Videos/remove-favorite-video/",
        // formData,
        {
          headers: {
            Authorization: "Bearer " + token,
          },
          data: {
            video_title: videoName,
          },
        }
      )
      .then((Response) => Response)
      .catch((Error) => Error);
  }
  return (
    <FavContext.Provider value={{ AddToFav, getUserFavVideos, deleteFavVideo }}>
      {props.children}
    </FavContext.Provider>
  );
}