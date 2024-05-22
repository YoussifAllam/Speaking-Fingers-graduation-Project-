import React from "react";
import { QueryClient, QueryClientProvider } from "react-query";
import Videos from "./Components/Videos/Videos";
import Favvideos from "./Components/Favvideos/Favvideos";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import Layout from "./Components/Layout/Layout";
import Videodetail from "./Components/Videodetail/Videodetail";
import FavContextProvider from "./Context/FavContext";
import UserContextProvider from "./Components/ContextToken/ContextToken";
import Homet from "./Components/Homet/Homet";
import Cnn from "./Components/Cnn/Cnn";
import Gtts from "./Components/Gtts/Gtts";
import VideoCon from "./Components/VideoCon/VideoCon";
import Login from "./Components/Login/Login";
import Register from "./Components/Regester/Regester";
import ForgetPassword from "./Components/ForgetPassword/ForgetPassword";
import ResetPassword from "./Components/Resetpassword/Resetpassword";
import PhotoToText from "./Components/PhotoToText/PhotoToText";
import Services from "./Components/Services/Services";
import Profile from "./Components/Profile/Profile";
import Verifyemail from "./Components/VerifyEmail/VerifyEmail";
export default function App() {
  let routers = createBrowserRouter([
    {
      path: "",
      element: <Layout />,
      children: [
        {path: "login", element: <Login /> },
        // {index:true, element: <Login /> },
        {path:"Verifyemail/:id", element: <Verifyemail /> },
        { path: "favvideos", element: <Favvideos /> },
        { path: "cnn", element: <Cnn /> },
        { path: "gtts", element: <Gtts /> },
        { path: "vidconv", element: <VideoCon /> },
        { index:true, element: <Register /> },
        { path: "homet", element: <Homet /> },
        { path: "videos", element: <Videos /> },
        { path: "forgetpassword", element: <ForgetPassword /> },
        { path: "photototext", element: <PhotoToText /> },
        { path: "services", element: <Services /> },
        { path: "profile", element: <Profile /> },
        { path: "resetpassword", element: <ResetPassword /> },
        { path: "videodetail/:title", element: <Videodetail /> },
      ],
    },
  ]);
  const client = new QueryClient();

  return (
    <QueryClientProvider client={client}>
      <UserContextProvider>

      <FavContextProvider>
        <RouterProvider router={routers}></RouterProvider>
      </FavContextProvider>
      </UserContextProvider>
  
    </QueryClientProvider>
  );
}
