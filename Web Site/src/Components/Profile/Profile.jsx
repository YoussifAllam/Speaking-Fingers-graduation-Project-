import {React,useContext, useEffect} from 'react'
import { UserContext } from '../ContextToken/ContextToken';
export default function Profile() {
  let{dataa,Usertoken}=useContext(UserContext)

  let{Settoken} =useContext(UserContext);
  useEffect(()=>{
    if( localStorage.getItem('usertoken')!=null ){
      Settoken (localStorage.getItem("usertoken"))
    }
  },[]);

console.log(dataa);


  return (
<div className='  cont '>

<div className='row'>

  <div className='col-md-4 prooimg'>
    
    <img className='prooof '  />
  <p className='namepaddin   text-marginn   '>{dataa?.username}</p> 
  
  </div>
  <div className='col-md-7 prooimg2'>

<label className='text-black  fw-bold' htmlFor="">Username</label>
      <div className='name-prof  mb-3   '> <p className='namepaddin'>{dataa?.username}</p> </div>
      <label className='text-black  fw-bold' htmlFor="" >Email</label>
      <div className='name-prof mb-3 '> <p className='namepaddin'> {dataa?.email}</p> </div>
      <label className='text-black fw-bold' htmlFor=""> Name</label>
      <div className='name-prof'> <p className='namepaddin '>{dataa?.name}</p> </div>
    


</div>

   
    </div>
</div>

  )
}
