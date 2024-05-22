
import React, { useState } from 'react';
import axios from 'axios';
import img4 from '../../Assets/Images/8c47ad697d57dd00e42291eea1c32828.png';
function App() {
  const [picture, setImage] = useState(null);
  const [result, setResult] = useState('');
  let [errMsg, setMsg] = useState('');
  const userToken = localStorage.getItem('usertoken');
  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleImageUpload = async () => {
    if (!picture) {
      alert('يرجى تحديد صورة أولاً');
      return;
    }
  
    const formData = new FormData();

    formData.append('picture', picture);
    console.log('FormData Entries:');
for (let pair of formData.entries()) {
  console.log(pair[0], pair[1]);
}
    // console.log('FormData:', formData);
    try {
      const response = await axios.post('https://youssifallam.pythonanywhere.com/api/CNN-api/predict_class', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `Bearer ${userToken}`
        }
      });
      console.log('Response:', response);
      // console.log(response);
  
      if (response.status === 401) {
        throw new Error('Unauthorized: تم رفض الوصول');
      }
  
      setResult(response.data.data.arabic_letter);
      console.log();
    } catch (error) {
      console.log('حدث خطأ أثناء استدعاء الخدمة:', error);
      console.log(error.response.data);
      setMsg(error.response.data.picture[0]);
    }
  };

  return ( 
    <div >
   
<div className=' container container-vv'>
<h2 className=' fw-bold '>Upload Image</h2>
<p className='weigrh'>You can upload an image from the browser so that the system can convert it into a letter</p>
<div className=' row  '>
  <div className='col-md-6 photoo2'>
    <img className='photoo4' src={img4} alt="" />
  </div>
  <div className='col-md-6 photoo3'>
  
            {errMsg!==''?<div className=' text-danger  '>{errMsg}</div>:""}
   <div className='upload'>  <input className='upload2  ' type="file" accept="image/*" onChange={handleImageChange} /> </div>
  
         <button className=' text-center mt-4 upload3   ' onClick={handleImageUpload}>Convert</button>
  
       <h3 className=' fw-bold  letter  '>Aletter:</h3>
      <div className='result'> {result!==""?<p className=' text-black text-center fw-bold    '>{result}</p>:""}</div>
  
  </div>
</div>
</div>
    </div>

   
  );
}

export default App;
