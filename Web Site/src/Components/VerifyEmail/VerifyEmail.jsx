import React, { useContext, useEffect, useState } from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { UserContext } from '../ContextToken/ContextToken';

export default function Verifyemail() {
  let { email } = useContext(UserContext);
  let Nav = useNavigate();

  async function Resendcode(val) {
    const emailuser = { email };
    axios.post("https:youssifallam.pythonanywhere.com/api/user/resend-otp/", emailuser)
      .catch((err) => {
        setMsg(err.response.data.message);
        setLoading(true);
      });
  }

  const { id } = useParams();
  useEffect(() => {
    formik3.setFieldValue('user_id', id);
  }, []);

  let validationSchema = Yup.object({
    otp: Yup.string().matches(/^[0-9]{1,4}$/, 'enter valid otp').required('otp is required'),
  });

  let [errMsg, setMsg] = useState("");
  let [Loading, setLoading] = useState(true);

  let formik3 = useFormik({
    initialValues: {
      otp: "",
    },
    onSubmit: Verifyemail,
    validationSchema,
  });

  async function Verifyemail(val) {
    setLoading(false);
    let req = await axios.post("https:youssifallam.pythonanywhere.com/api/user/confirm-email/", val)
      .catch((err) => {
        setMsg(err.response.data.message);
        setLoading(true);
      });

    if (req.request.statusText === "OK") {
      Nav('/login');
    }
  }

  return (
    <div style={{ backgroundColor: '#0caed438', minHeight: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <div className='conta text-center'>
        <div className='d-flex flex-column justify-content-center align-item-center all'>
          <h2 className='fw-bold'>Almost there</h2>
          <p className='mt-3 mb-3 '>Please enter the 4-digit code sent to your email <a href="mailto:contact.uiuxexperts@gmail.com">contact.uiuxexperts@gmail.com</a> for verification.</p>

          <form onSubmit={formik3.handleSubmit}>
            {errMsg !== '' ? <div className='alert alert-danger'>{errMsg}</div> : null}

            <div class="input-container">
              <input onChange={formik3.handleChange} value={formik3.values.otp} type='number' name='otp' className="inputtt" />
            </div>

            <button type='submit' className='button design mb-4 mt-4'>Verify OTP</button>
          </form>

          <p className='fw-bold'>Didn’t receive any code? <span className='spancolor cursor-pointer' onClick={Resendcode}>Resend Again</span></p>
        </div>
      </div>
    </div>
  );
}

