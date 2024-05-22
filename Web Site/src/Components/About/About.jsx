import style from "./About.module.css";
import { Link } from "react-router-dom";
function About() {
  return (
    <div className={style.bodyy}>
      <div className="cont3">
        <div className="row">
          <div className={`${style.paras} col-md-6 `}>
            <h2 className={`my-5`}>Enable Communication Between Humans</h2>
            <div className="container">
              <div className="row">
                <div className="col-md-4">
                  <p>
                    We hope you have benefited from your visiting to our Website
                    about convert sign language into text and audios.
                  </p>
                </div>
                <div className="col-md-4">
                  <p>
                    These techniques are an effective way to empower people and
                    improve their daily quality of life by facilitating
                    communication and access to information
                  </p>
                </div>
                <div className="col-md-4">
                  <p>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Praesentium, deleniti.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div className={`${style.pic} col-md-6 `}>
            <img
              src={require("../../Assets/Images/1000211614-removebg-preview.png")}
              className="card-img-top "
              alt="image"
            />
          </div>
        </div>
      </div>
      {/* footer */}
      <div className={style.footer}>
        <div className="container ">
          <div className="row">
            <div className="col-md-4">
              <div className={`mx-5 p-5 ${style.logo}`}>
                <img
                  src={require("../../Assets/Images/LOGO.png")}
                  width="50 px"
                  alt="image"
                />
                <p className={style.copyright}>
                  Copyright ©2024 All rights reserved
                </p>
              </div>
            </div>
            <div className="col-md-4 p-5">
              <ul className={`${style.list1}  list-unstyled `}>
                <span className={`ms-3 my-1 ${style.word} `}> pages</span>
                <li className="mx-3 my-1">
                  <a href="#homesec">Home</a>
                </li>
                <li className="mx-3 my-1">
                  <Link to="/videos">Videos</Link>
                </li>
                <li className="mx-3 my-1">
                  <Link to="/favvideos">Favorite videos</Link>
                </li>
              </ul>
            </div>
            <div className="col-md-4 p-5">
              <ul className={`${style.list2} list-unstyled `}>
                <span className={`ms-3 my-1 ${style.word} `}>
                  Main services
                </span>
                <li className="mx-3 my-1">
                  <Link to="/photototext"> Picture conversion</Link>
                </li>
                <li className="mx-3 my-1">
                  <Link to="/gtts">Text conversion</Link>
                </li>

                <li className="mx-3 my-1">
                  <Link to="/vidconv">Vido conversion</Link>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
