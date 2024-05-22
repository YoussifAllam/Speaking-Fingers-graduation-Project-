import style from "./Login.module.css";
import React, { useState, useContext } from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import img2 from '../../Assets/Images/WhatsApp Image 2024-03-17 at 12.59.27 AM.jpeg';
import { UserContext } from '../ContextToken/ContextToken';

export default function Login() {
  let{Settoken,Settoken2,setdataa}=useContext(UserContext)
  let { setEmailuser } = useContext(UserContext);
  let Nav = useNavigate();

  let validationSchema = Yup.object({
    email: Yup.string().required('Email is required').matches(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i, 'Enter valid email'),
    password: Yup.string().required("Password is required").matches(/^[A-z][a-z0-9A-Z!@#$%^&*()_-]{6,16}$/,"enter valid password"),
 
  });

  let [errMsg, setMsg] = useState('');
  let [Loading, setLoading] = useState(true);

  let formik = useFormik({
    initialValues: {

  email:"",
password:"",
 
    },
    onSubmit: registerApi,
    validationSchema,
  });

  async function registerApi(value) {
    setLoading(false);
    let req = await axios.post('https://youssifallam.pythonanywhere.com/api/user/login/', value)
    .catch(function(error) {
      setMsg(error.response.data.message);
      // console.log(error);
  
      setLoading(true)
   


    });
    console.log(req);

 if(req.request.statusText=="OK"){

  localStorage.setItem('usertoken', req.data.tokens.access)
  Settoken(req.data.tokens.access)
  setdataa(req.data.user)
  // Settoken2(req.data.tokens.refresh  )
  // localStorage.setItem('usertoken1', req.data.tokens.refresh )
  Nav('/homet'); 
  }

}


  return (

    <div className="container   d-flex     py-5">
      <div className='row      '>
        <div className={`${style.color2} col-md-5 `}>
        <div className=' d-flex justify-content-between '>
    <div className=' mt-2  d-flex justify-content-between '>  
      <h2 className=' fw-bold   ' >Welcome back</h2>
      </div>
      {errMsg!==''?<div className=' text-danger  '>{errMsg}</div>:""}
</div>

<div>
<span className=''>sign in to access your account</span></div>




<form onSubmit={formik.handleSubmit} >


<div  >
<label htmlFor="email"></label>
 {/* <i class="fa-solid fa-envelope"></i> */}
 <div className={`${style.email}`}>
 <input  placeholder='     Valid email' value={formik.values.email}  onBlur={formik.handleBlur} onChange={formik.handleChange} className='form-control' type="text" name='email' id='email'/>
 </div>

 {formik.errors.email&& formik.touched.email?<p className='text-danger   '>{formik.errors.email}</p>:""}

 </div>


 <div className='password'>
 <label htmlFor="password"></label>
 {/* <i class="fa-solid fa-lock"></i> */}
 <input  placeholder='     Strong Password' value={formik.values.password}   onBlur={formik.handleBlur} onChange={formik.handleChange} className='form-control' type="password" name='password' id='password'/>

 {formik.errors.password&& formik.touched.password?<p className='text-danger  '>{formik.errors.password}</p>:""}

 </div>

 <div className=' pb-4 pt-2  d-flex justify-content-around '>
  <div>
  <input type="checkbox" name="" id="" />    <label htmlFor="">Remember me</label> </div>

  <div>
    <a href="../ForgetPassword/">forget password?</a></div>
   </div>



 {Loading? <button disabled={!(formik.isValid&&formik.dirty)} type='submit' className={`${style.button}  w-100  d-block  `}>Next </button>:<button  className='button ' type='button'><i class="fa-solid fa-spinner"></i></button> }
 <p className=' text-center my-3 '>New Member? <a href='.'>Regester Now</a></p>

 </form>


        </div>
        <div className={`col-md-4 ${style.photo} `}>
         <div  className={` ${style.photo} `}>
<img className='' src={img2} alt="" />
 </div>ّّ
        </div>
      </div>
    </div>
  )}

