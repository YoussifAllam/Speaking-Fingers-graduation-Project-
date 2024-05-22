import React from 'react'
import Navpar from '../Navbar/Navbar'
import { Outlet } from 'react-router-dom'
import Footer from '../Footer/Footer'
import {UserContext} from "../ContextToken/ContextToken"
 import{useEffect } from 'react'
 import{useContext} from 'react'


export default function Layout() {
  let{Settoken} =useContext(UserContext);
  useEffect(()=>{
    if( localStorage.getItem('usertoken')!=null ){
      Settoken (localStorage.getItem("usertoken"))
    }
  },[]);
  return (
    <div>

<Navpar></Navpar>
    <Outlet></Outlet>

    </div>
  )
}