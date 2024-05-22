import react from "react";
import style from "./Spiner.module.css";
export default function Spiner() {
  return (
    <>
      <div className=" bg-white d-flex justify-content-center align-items-center position-fixed top-0 bottom-0 end-0 start-0">
        <span className="loader"></span>
      </div>
    </>
  );
}
