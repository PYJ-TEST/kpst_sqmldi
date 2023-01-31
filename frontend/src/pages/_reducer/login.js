import { createStore } from 'redux';

// 액션 타입 (접두사: 이름 중복 방지)
const ISLOGIN = 'login/ISLOGIN';

// 액션 생성함수(액션 객체에는 type 값 필수)
export const isLogin = message => ({ 
    type: ISLOGIN,
    message: message
});

// 초기 상태
const initialState = {
    bool: false
};

// 리듀서
export default function changeState(state=initialState, action){
    switch(action.type){
        case ISLOGIN:
            return {
                bool: action.message === 'success' ? !state.bool : state.bool
            }
        default:
            return state
    }
}
