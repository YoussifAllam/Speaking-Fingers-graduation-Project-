import { useState } from "react";
import style from "./Homet.module.css";
import About from "../About/About";
import Services from "../Services/Services";
import Videos from "../Videos/Videos";
function Home() {
  return (
    <>
      <div className={style.bodyy} id="homesec">
        <div className="container ">
          <div className="row">
            <div className="col-md-6 ">
              <p className={`${style.inter} ${style.homepara1}`}>
                Communicate With Deaf And Hard Of Hearing People
              </p>

              <p className={`${style.homepara2} ${style.inter}`}>
                Artificial Intelligence Supported Sign Language Translator
                System e enable hearing impaired and deaf individuals who have
                difficulty in understanding what they read or are illiterate to
                access information, services and video content with the ai
                powered sign language , which is their mother tongue
              </p>
              <p className={style.lightfont}>
                With the development of technology, it has become possible to
                convert sign language into text or audio recording, and this
                facilitates communication and understanding between people.
              </p>
              {/* <button className={`${style.btnhome} `}>Get Started</button> */}
              <button
                type="button"
                className={`${style.btnhome} btn btn-primary`}
              >
                <a className="gotoservices" href="./services"> Get Started</a>
               
              </button>
            </div>
            <div className="col-md-6">
              <img
                className={style.homeimg2}
                src={require("../../Assets/Images/1000203764-removebg-preview.png")}
                alt="image"
                width="500px"
              />
              ;
            </div>
          </div>
        </div>
      </div>
      <div className="my-5">
        <Services />
      </div>
      <div className="my-5">
        <Videos />
      </div>
      <div className="my-5">
        <About />
      </div>
    </>
  );
}

export default Home;
