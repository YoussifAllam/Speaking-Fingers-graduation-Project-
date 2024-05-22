import style from "./VideoCon.module.css";

function VideoCon() {
  return (
    <>
      <div>
        <h3> ay haga</h3>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo voluptate
          ad asperiores maxime nemo rem delectus aliquam exercitationem
          necessitatibus ab.
        </p>
      </div>

      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <button className="btn btn-info ">upload video</button>
            <div className={style.backvideo}>video</div>
          </div>
          <div className="col-md-6">
            <textarea
              name=""
              id=""
              style={{ width: "500px", minHeight: "200px" }}
            ></textarea>
          </div>
        </div>
      </div>
    </>
  );
}

export default VideoCon;
