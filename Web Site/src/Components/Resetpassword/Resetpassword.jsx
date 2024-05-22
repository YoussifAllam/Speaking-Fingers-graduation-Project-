import React, {useContext, useState } from 'react'
import style from "./Resetpassword.module.css";
import { useFormik } from 'formik'
import * as Yup from 'yup'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import img from '../../Assets/Images/WhatsApp Image 2024-03-17 at 12.59.27 AM.jpeg'
import { useParams } from 'react-router-dom'
import { UserContext } from '../ContextToken/ContextToken';
export default function Register() {

let Nav=useNavigate()
  let{Usertoken}=useContext(UserContext)

  let validationSchema = Yup.object({

    password: Yup.string().required("password is required").matches(/^[A-z][a-z0-9A-Z!@#$%^&*()_-]{6,16}$/,"enter valid password"),
    confirmpassword: Yup.string().required("RePassword is required").oneOf([Yup.ref('password')]),


  })
 let[errMsg,setMsg]=useState("")
 let[Loading,setLoading]=useState(true)


 
  let formik=useFormik(
{
initialValues:{
  password:"",
  confirmpassword:"",

 
},

  
onSubmit:registerApi,

validationSchema
}
 )



async function registerApi(value) {
    setLoading(false);
    let req = await axios.post(`https://youssifallam.pythonanywhere.com/api/reset_password/?${Usertoken}`, value)
    .catch(function(error) {
      setMsg(error.response.data.message);
  
      setLoading(true)
   
  

    });
 
console.log(req);
 if(req.request.statusText=="OK"){

  Nav('/Home'); 
  }

}


  return (

    <div className='  '>



  <div className='container   d-flex justify-content-around      all  py-5'>

<div className=' color2  margin  '>

  <div className=' d-flex justify-content-between '>
    <div className=' mt-2  d-flex justify-content-between '>  
      <h2 className=' fw-bold   ' >Reset Password</h2>
      </div>
      {errMsg!==''?<div className=' text-danger  '>{errMsg}</div>:""}
</div>

<div>
<span>Create a new password</span></div>




<form onSubmit={formik.handleSubmit} >








<div className='password'>
<label htmlFor="password"></label>
{/* <i class="fa-solid fa-lock"></i> */}
<input  placeholder='     Strong Password' value={formik.values.password}   onBlur={formik.handleBlur} onChange={formik.handleChange} className='form-control' type="password" name='password' id='password'/>

{formik.errors.password&& formik.touched.password?<p className='text-danger  '>{formik.errors.password}</p>:""}

</div>

<div className='confirmpassword'>
<label htmlFor="confirmpassword"></label>
{/* <i class="fa-solid fa-lock"></i> */}
<input  placeholder='     Strong Password' value={formik.values.confirmpassword}   onBlur={formik.handleBlur} onChange={formik.handleChange} className='form-control' type="password" name='confirmpassword' id='confirmpassword'/>

{formik.errors.password&& formik.touched.password?<p className='text-danger  '>{formik.errors.confirmpassword}</p>:""}

</div>


<p className=' text-center my-3 '><input type="checkbox" name="" id="" />  By checking the box you agree to our <span className='span'>Terms</span> and <span className='span' >Conditions</span>.</p>

{Loading? <button disabled={!(formik.isValid&&formik.dirty)} type='submit' className='button w-100  d-block  '>Next </button>:<button  className='button ' type='button'><i class="fa-solid fa-spinner"></i></button> }



</form>

</div>

<div  className='photo'>
<img className='w-100' src={img} alt="" />
</div>ّّ

</div>ّ


    </div>

  )}












