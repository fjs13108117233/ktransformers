import axios, { AxiosInstance } from 'axios';
import {baseURL} from '@/conf/config';
import store from '@/store';

const apiClient: AxiosInstance = axios.create({
    baseURL: baseURL,
    // baseURL: '/api',
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true,
});

// Add request interceptor to automatically include auth token
apiClient.interceptors.request.use(
    (config) => {
        const token = store.getters.token;
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default apiClient;
