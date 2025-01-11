import axios from 'axios';

const baseUrl = 'http://localhost:3307';
const user = "users"

const createUser = async (newUser) => {
    const response = await axios.post(`${baseUrl}/${user}`, newUser);
    return response;
};

const getUser = async (id, jwt_token) => {
    const response = await axios.get(`${baseUrl}/${user}/${id}`, jwt_token);
    return response;
};

const loginUser = async (userCredentials) => {
    const response = await axios.post(`${baseUrl}/login`, userCredentials);
    return response;
}

const updateUser = async (id, newUser, jwt_token) => {
    // note that user has the fields username, email, and password
    console.log(user)
    const response = await axios.patch(`${baseUrl}/${user}/${id}`, newUser, jwt_token);
    return response;
}

const exportedObjects = { createUser, getUser, loginUser, updateUser };

export default exportedObjects;