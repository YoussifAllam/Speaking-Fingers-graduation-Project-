import { Link } from "react-router-dom";
import React, { useContext, useEffect, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import img5 from "../../Assets/Images/8c47ad697d57dd00e42291eea1c32828.png"
import { UserContext } from '../ContextToken/ContextToken';
import style from "./Navbar.module.css";
function Navbar() {
   let navigate=useNavigate()
  let{Usertoken,Settoken}=useContext(UserContext)
  function LogOut(){
    localStorage.setItem('usertoken',null)
    Settoken(null)
    navigate('/login')
  }

  return (

    
    <nav className="navbar navbar-expand-lg bg-body-tertiary ">
      <div className="container-fluid">
        <div className={`  mt-1 ${style.logo}`}>
          <img
            src={require("../../Assets/Images/LOGO.png")}
            width="70 px"
            alt="image"
          />
        </div>
        <button


          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>  
        
        
          {Usertoken!==null?  <div className="collapse navbar-collapse" id="navbarNav">

    
    
    
        
<ul className="navbar-nav m-auto">
<li className="nav-item mt-3  ">
  <Link className="m-3 me-3" to="/homet">
    Home
  </Link>
</li>

<li className="nav-item mt-3 ">
  <Link className="m-3 " to="/services">
    Services
  </Link>
</li>
<li className="nav-item mt-3 ">
  <Link className="m-3 " to="/videos">
    Videos
  </Link>
</li>
<li className="nav-item logggout2  mt-3 ">
  <Link className="m-3 " to="/favvideos">
    Favorite videos
  </Link>
</li>
<li class="px-4 nav-item  logggout navvvvv ">
  <spqn class=" nav-link active bluuuu cursor-pointer" onClick={LogOut} aria-current="page" to="Signup">Logout </spqn>
</li>
   
{/* <Link  class="navbar-brand nav-logo    " to="/profile"><img   className={`  ${style.logo} `} src={img5} alt="" /></Link> */}
</ul>


<NavLink  class="navbar-brand nav-logo    " to="/profile"><img  className="logo nnn nnn2" src={img5} alt="" /></NavLink>


</div> : <ul class="navbar-nav me-auto mb-2 nav-enter mb-lg-0">
        <li class=" px-4 nav-item">
          <NavLink class="    nav-link active" aria-current="page" to="login">Log in</NavLink>
        </li>
        <li class="nav-item">
          <NavLink class="  nav-link active" aria-current="page" to=".">Sign up </NavLink>
        </li>
     
      
 
        
        </ul>
      }
      
      </div>
    </nav>
  );
}

export default Navbar;
