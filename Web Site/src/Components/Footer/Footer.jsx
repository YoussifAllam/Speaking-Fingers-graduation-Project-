import { Link } from "react-router-dom";
import style from "./Footer.module.css";
function Footer() {
  return (
    <>
      <div className="container">
        <div className="row">
          <div className="col-md-4">
            <div className="mx-5 p-5">
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
          <div className="col-md-4">
            <ul className="p-5 ">
              <span>pages</span>
              <li className="mx-3">
                <Link to="homet">homet</Link>
              </li>
              <li className="mx-3">
                <Link to="videos">videos</Link>
              </li>
              <li className="mx-3">
                <Link to="favvideos">fav videos</Link>
              </li>
            </ul>
          </div>
          <div className="col-md-4 p-5">
            <ul>
              <span>main services</span>
              <li className="mx-3">
                <Link to="cnn"> picture conversion</Link>
              </li>
              <li className="mx-3">
                <Link to="gtts">text conversion</Link>
              </li>

              <li className="mx-3">
                <Link to="vidconv">vido conversion</Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </>
  );
}

export default Footer;
