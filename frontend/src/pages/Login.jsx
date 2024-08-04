import React, { useState,useContext, useEffect } from 'react'
import {Container, Row, Col, Form, FormGroup, Button} from "reactstrap";

import {Link,useNavigate  } from "react-router-dom";
import "../styles/login.css";

import loginImg from "../assets/images/login.png";
import userIcon from "../assets/images/user.png";

import { AuthContext } from '../context/AuthContext';
import  {BASE_URL} from "../utils/config";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Cookies from 'js-cookie';


const Login = () => {
  const [credentials,setCredentials]=useState({
    username:undefined,
    password:undefined,
  })
  
  useEffect(() => {
    get_cookie()
  }, [])
      function get_cookie(){
      const res =  fetch(`${BASE_URL}/auth/session`, {
        method: 'get',
        headers: {
          'content-type':'application/json',
        },
        credentials:'include'
      })
  }
  
    const navigate=useNavigate();
    const {dispatch}=useContext(AuthContext); /* now basically we will receive all the values given by AuthContext.provider */

  const handleChange=e=>{
    setCredentials(prev=>({ ...prev, [e.target.id]:e.target.value}))
};

  
const handleClick= async e=>{
      e.preventDefault();
  dispatch({ type: 'LOGIN_START' })
 
  try {
    const csrftoken = Cookies.get('csrftoken')
          const res= await fetch(`${BASE_URL}/auth/login`,{
            method:'post',
            headers:{
              'content-type': 'application/json',
              'X-CSRFToken': csrftoken
            },
            credentials:"include",
            body:JSON.stringify(credentials)  /* when we need to send data to server or receive data form server we stringify data from the object literal form to the JSON string form  */
          })   
         

          /* the response received from the backend */
          const result=await res.json();

          if(!res.ok){ 
            toast.error(result.message, {
              position: "top-right",
              autoClose: 5000,
              hideProgressBar: false,
              closeOnClick: true,
              pauseOnHover: true,
              draggable: true,
              progress: undefined,
              theme: "light",
              });
            }
          
          else {
            console.log(result)
          dispatch({type:'LOGIN_SUCCESS',payload:result.data});
          navigate('/')
          // console.log(JSON.stringify(result.data) + "-->" +"user data");
          }

      } catch (error) {
          dispatch({type:'LOGIN_FAILURE',payload:error.message})
      }
}


  return <section>
    <Container>
      <Row>
        <Col lg='8' className='m-auto'>
            <div className="login__container d-flex justify-content-between">
               <div className="login__img">
                <img src={loginImg} alt="" />
               </div>

               <div className="login__form">
                <div className="user">
                  <img src={userIcon} alt="" />
                </div>
                <h2>Login</h2>
              
                <Form onSubmit={handleClick}>  
                  <FormGroup>
                    <input type="text" placeholder='Username' required id='username' onChange={handleChange} />
                  </FormGroup>
                  <FormGroup>
                    <input type="password" placeholder='Password' required id='password' onChange={handleChange} />
                  </FormGroup>
                      <Button className='btn secondary__btn auth__btn' type='submit'>Login</Button>
                </Form>
                <p>Don't have an account? <Link to='/register'>Create</Link></p>
               </div>
            </div>
        </Col>
      </Row>
    </Container>
    <ToastContainer/>
  </section>
}

export default Login