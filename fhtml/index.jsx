import React from "react";
import "./style.css";

export const Desktop = () => {
  return (
    <div className="desktop">
      <div className="div">
        <div className="overlap">
          <div className="text-wrapper">HOME</div>
          <div className="text-wrapper-2">ABOUT</div>
          <div className="text-wrapper-3">CONTACT</div>
          <div className="frame">
            <div className="text-wrapper-4">SIGN UP</div>
          </div>
          <p className="LEND-AND-EARN">
            <span className="span">LEND AND </span>
            <span className="text-wrapper-5">EARN</span>
          </p>
        </div>
        <div className="overlap-group">
          <p className="NEED-a-LOAN-ENTER">
            <span className="text-wrapper-6">
              NEED&nbsp;&nbsp;A&nbsp;&nbsp;LOAN
              <br />
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </span>
            <span className="text-wrapper-7">ENTER THE ZONE</span>
          </p>
          <img className="vector" alt="Vector" src="vector.svg" />
          <img className="img" alt="Vector" src="image.svg" />
          <img className="vector-2" alt="Vector" src="vector-2.svg" />
          <img className="vector-3" alt="Vector" src="vector-3.svg" />
        </div>
        <div className="group-wrapper">
          <div className="group">
            <div className="frame-2">
              <div className="text-wrapper-8">LEND</div>
              <img className="gemini-generated" alt="Gemini generated" src="gemini-generated-image-1-1.png" />
            </div>
            <div className="overlap-group-wrapper">
              <div className="overlap-group-2">
                <div className="text-wrapper-9">BORROW</div>
                <img className="gemini-generated-2" alt="Gemini generated" src="gemini-generated-image-2-1.png" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
