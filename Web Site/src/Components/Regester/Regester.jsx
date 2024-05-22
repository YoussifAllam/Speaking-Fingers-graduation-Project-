

import React, { useState, useContext } from 'react';
import style from "./Regester.module.css";
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import img2 from '../../Assets/Images/WhatsApp Image 2024-03-17 at 12.59.27 AM.jpeg';
import { UserContext } from '../ContextToken/ContextToken';

export default function Register() {
  let { setEmailuser,dataa,setdataa,Settoken2,Usertoken2 } = useContext(UserContext);
  let Nav = useNavigate();

  let validationSchema = Yup.object({
    name: Yup.string().required('Name is required').min(3, 'Min Length must be greater than 3 letters').max(20, 'Max Length must be less than 20 letters'),
        email: Yup.string().email('email is invalid').required('email is required'),
        // email: Yup.string().required('Email is required').matches(/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i, 'Enter valid email'),
        password: Yup.string().required("Password is required").matches(/^[A-z][a-z0-9A-Z!@#$%^&*()_-]{6,16}$/,"enter valid password"),
        // rePassword: Yup.string().required("RePassword is required").oneOf([Yup.ref('password')]),
    
  });

  let [errMsg, setMsg] = useState('');
  let [Loading, setLoading] = useState(true);

  let [daaaata, setdaaaata] = useState('');
  let formik = useFormik({
    initialValues: {
  name:"",
  email:"",
password:"",
 
    },
    onSubmit: registerApi,
    validationSchema,
  });

  async function registerApi(value) {
    setLoading(false);
    let req = await axios.post('https://youssifallam.pythonanywhere.com/api/users/', value)
    .catch(function (error) {
      setMsg(error.response.data.message);

      setLoading(true);
    });
  console.log(req);

    if (req.request.statusText === 'Created') {
      const id = req.data.user.id;

      setEmailuser(value.email);
      localStorage.setItem('usertoken2', req.data.tokens.refresh)
      // Settoken2(req.data.tokens.refresh)
      Nav(`/Verifyemail/${id}`);
     
    }
  } 

  return (
    <div className='container  d-flex     py-5'>
      <div className='row      '>
        <div className={`${style.color2} col-md-5 `}>
        <div className=' d-flex justify-content-between '>
    <div className=' mt-2  d-flex justify-content-between '>  
      <h2 className=' fw-bold   ' >Get Started</h2>
      </div>
      {errMsg!==''?<div className=' text-danger  '>{errMsg}</div>:""}
</div>

<div>
<span>by creating a free account</span></div>




<form onSubmit={formik.handleSubmit} >




<div className='name'>
<label htmlFor="name"></label>
{/* <i class="fa-solid fa-user"></i> */}
<input placeholder='     Full name' value={formik.values.name} onBlur={formik.handleBlur} onChange={formik.handleChange} className='form-control' type="text" name='name' id='name'/>

{formik.errors.name&& formik.touched.name?<p className='text-danger'>{formik.errors.name}</p>:""}


</div>
<div className='email'>
<label htmlFor="email"></label>
 {/* <i class="fa-solid fa-envelope"></i> */}
 <input placeholder='     Valid email' value={formik.values.email}  onBlur={formik.handleBlur} onChange={formik.handleChange} className='form-control' type="text" name='email' id='email'/>
 {formik.errors.email&& formik.touched.email?<p className='text-danger   '>{formik.errors.email}</p>:""}

 </div>



 <div className='password'>
 <label htmlFor="password"></label>
 {/* <i class="fa-solid fa-lock"></i> */}
 <input  placeholder='     Strong Password' value={formik.values.password}   onBlur={formik.handleBlur} onChange={formik.handleChange} className='form-control' type="password" name='password' id='password'/>

 {formik.errors.password&& formik.touched.password?<p className='text-danger  '>{formik.errors.password}</p>:""}

 </div>


 <p className=' text-center my-3 '><input type="checkbox" name="" id="" />  By checking the box you agree to our <span className='span'>Terms</span> and <span className='span' >Conditions</span>.</p>

 {Loading? <button disabled={!(formik.isValid&&formik.dirty)} type='submit' className={` ${style.button} w-100  d-block  `}>Next </button>:<button  className='button ' type='button'><i class="fa-solid fa-spinner"></i></button> }
 <p className=' text-center my-3 '>Already a member? <a href='/login'>Log In</a>

 </p>

 </form>


        </div>
        <div className='col-md-4 photo'>
         <div  className='photo'>
<img className='' src={img2} alt="" />
 </div>ّّ
        </div>
      </div>
    </div>
  );
}