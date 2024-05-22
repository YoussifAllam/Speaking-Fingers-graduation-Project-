import React, { useState } from "react";
import axios from "axios";
import style from "./Gtts.module.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHome } from "@fortawesome/free-solid-svg-icons";
import { FaBeer } from "react-icons/fa";
import { FaStar } from "react-icons/fa";
function Gtts() {
  const [textInput, setTextInput] = useState("");
  const [audioURL, setAudioURL] = useState("");

  const language = "ar";

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const formData = new FormData();
      formData.append("text", textInput);
      formData.append("language", language);

      const response = await axios.post(
        "https://youssifallam.pythonanywhere.com/api/v1/GTTS/text-to-speech/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setAudioURL(response.data.URL);
    } catch (error) {
      console.error("error", error);
    }
  };

  const handleClear = () => {
    setTextInput("");
  };

  return (
    <>
      <div className="conta3">
        <h2 className={style.heading}>Convert text</h2>
        <p className={style.para}>
          Enter the words here then the system convert the words into an audio
          recording that you can listen it directly
        </p>
      </div>
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <img
              className={style.pic}
              src={require("../../Assets/Images/e1ab71c6-ad80-4ad0-a3b0-962150f36385.jpg")}
              alt="image"
              width="500px"
            />
          </div>
          <div className={`${style.part2} col-md-6`}>
            <form onSubmit={handleSubmit}>
              <div>
                <label className={style.labeltext}>Text</label>
              </div>
              <div className={style.inputContainer}>
                <textarea
                  className={style.area}
                  value={textInput}
                  onChange={(e) => setTextInput(e.target.value)}
                  style={{ width: "500px", minHeight: "200px" }}
                />
                {textInput && (
                  <button
                    type="button"
                    onClick={handleClear}
                    className={style.clearbtn}
                  >
                    X
                  </button>
                )}
              </div>
              <button className={`${style.convertbtn} btn`} type="submit">
                Convert
              </button>
            </form>
            {audioURL && (
              <div>
                <label className={style.labeltext}>Audio</label>
                <audio className={style.audioControl} key={audioURL} controls>
                  <source src={audioURL} type="audio/mpeg" />
                  Your browser does not support the audio element.
                </audio>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}

export default Gtts;
