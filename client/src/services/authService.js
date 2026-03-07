import api from './api';

export const login = async (email, password) => {
  const params = new URLSearchParams()
  params.append('username', email)
  params.append('password', password)

  const response = await api.post('/auth/token', params, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  })

  const token = response.data.access_token
  localStorage.setItem('access_token', token)
  return token
}
export const register = async (email, password, confirmPassword) => {
    
    if (password !== confirmPassword){
        window.alert('Passwords do not match!');
        return;
    }
    if (password.length == 0 || email.length == 0){
        window.alert('Email and Password cannot be empty!');
        return;
    }
    const newUser = {
        email: email,
        password: password,
    }
    const response = await api.post('/auth/register', newUser);
    return response.data;
};