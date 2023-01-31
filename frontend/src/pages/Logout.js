import React, { useState } from "react";
import axios from "axios";

function Logout(props){
    const url = 'http://localhost:8000/accounts/logout/';
    // console.log(props.isLogin)
    // const isLogin = props.isLogin;
    const [isLogin, setIsLogin] = useState(props.isLogin);
    const [message, setMessage] = useState('');

    const handleLogout = (e) =>{
        e.preventDefault();
        sessionStorage.removeItem('user_id');
        console.log('세션 제거');

        axios.post(url, {})
            .then((result)=> {
                // console.log(result.data);
                if (result.data.message === 'success') {
                    setMessage('로그아웃에 성공하였습니다.');
                    setIsLogin(false);
                }
            })
            .catch((error)=> {
                console.log(error);
            });
    }

    return (
        <div>
            <button onClick={handleLogout}>로그아웃</button>
            {message}
        </div>
    );
}

export default Logout;