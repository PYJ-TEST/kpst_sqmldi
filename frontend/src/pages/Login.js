import React, { useState } from "react";
import axios from "axios";
import Logout from "./Logout";

function Login(){
    const url = 'http://localhost:8000/accounts/login/';
    const [message, setMessage] = useState('');
    const [isLogin, setIsLogin] = useState(false);
    
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
                console.log(result.data);
                if (result.data.message === 'success') {
                    sessionStorage.setItem('user_id', e.target['user_id'].value);
                    setIsLogin(true);
                    setMessage('로그인에 성공하였습니다');
                }
            })
            .catch((error)=> {
                console.log(error);
            });
    };

    return (
        <div>
            {isLogin ? <></> :
                <form method="post" onSubmit={handleSubmit}>
                    <input type="text" name="user_id" placeholder="id 입력" />
                    <input type="password" name="user_password" placeholder="pw 입력" />
                    <button type="submit">로그인</button>
                </form>
            }
            {message}
            {isLogin ? <Logout isLogin={isLogin}/> : <></>}
        </div>
    );
};

export default Login;