// import { div } from '@tensorflow/tfjs'
import React from 'react'

export default function Tichnique() {
  return (

    <div className='cont2'>
   <div className=' container   '>


<div className=' text-center mt-5 '>
  
  
   <h2 className=' liine fw-bold position-relative  '>Amazing <span className='bluee'>Services & Features</span> For You.</h2>


      <p className='paragraphh'>Our services play a vital role in facilitating communication and <br></br>enabling access for people with special needs, by converting <br></br>video and text into formats understandable to them, which <br></br>promotes communication and positive interaction between all<br></br> segments of society.</p>
    </div>




      
      <div className='row justify-content-center container-buttom '>

        <div className='divv1 col-md-3 '>
          <div className='icon-cameraa text-center mt-2 '>   <i class="fa-solid fa-camera"></i></div>
     
          <h3  className=' fw-bold mb-3 lll '>Use The Camera</h3>
          <p className='cameraaa'>you can open The Camera<br></br>video from your<br></br> device to convert it<br></br> into a text then<br></br> convert the text into<br></br> an audio recording</p>
         <a href='../Login' className='anccor fw-bold' >Start-> </a>
        </div>

        <div className='divv1 col-md-3  divv2 '>
          <div className='icon-cameraa text-center mt-2'><i class="fa-solid fa-microphone"></i></div>
          <h3 className='mb-5 fw-bold lll '>Text to audio</h3>
          <p className='cameraaa cameraaa2  '>convert text into audio recording </p>
       <a href='../gtts '  className='anccor fw-bold'>Start-> </a>
        </div>
       
        <div className='divv1 col-md-3  '>
          <div className='icon-cameraa text-center mt-2' ><i class="fa-solid fa-photo-film"></i></div>
          <h3 className=' fw-bold mb-5 lll '>Upload image</h3>
          <p className='cameraaa mb-4 '>you can upload an<br></br> image from your device <br></br> then convert it into a<br></br>  letter</p>
         <a href='../photototext' className='anccor  fw-bold '>Start-> </a>
        </div>
        
      </div>
    </div>

    </div>
 
  )
}
