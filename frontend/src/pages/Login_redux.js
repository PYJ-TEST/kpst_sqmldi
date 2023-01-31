import React, { useState,useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { isLogin } from './_reducer/login'
import axios from "axios";
import Logout from "./Logout";

function Login(){
    const url = 'http://localhost:8000/accounts/login/';
    const [message, setMessage] = useState('');

    const { bool } = useSelector(state => ({
        bool: state.changeState.bool,
    }));

    const dispatch = useDispatch();
    const onIsLogin = message => dispatch(isLogin(message));

    const handleSubmit = (e) =>{
        e.preventDefault();

        axios.post(url, {
            'user_id': e.target['user_id'].value,
            'user_password': e.target['user_password'].value,
        },{
            headers: {
                "Content-Type": "application/json",
            }
        })
            .then((result)=> {
                let message = result.data.message;
                if (message === 'success') {
                    sessionStorage.setItem('user_id', e.target['user_id'].value);
                    onIsLogin(message);
                    
                    console.log('change: '+bool);
                    setMessage('로그인에 성공하였습니다');
                }
            })
            .catch((error)=> {
                console.log("ERROR:"+error);
            });
    };

    return (
        <div>
            {bool ? <></> :
                <form method="post" onSubmit={handleSubmit}>
                    <input type="text" name="user_id" placeholder="id 입력" />
                    <input type="password" name="user_password" placeholder="pw 입력" />
                    <button type="submit">로그인</button>
                </form>
            }
            {message}
            {bool ? <Logout /> : <></>}
        </div>
    );
};

export default Login;