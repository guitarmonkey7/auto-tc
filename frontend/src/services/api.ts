import axios from 'axios';
import { Task, Transaction, User, ApiResponse } from '../types';
import { API_URL } from '../config';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add request interceptor to include auth token
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

// Tasks API
export const tasksApi = {
    getTasks: () => api.get<ApiResponse<Task[]>>('/tasks'),
    getTask: (id: number) => api.get<ApiResponse<Task>>(`/tasks/${id}`),
    createTask: (task: Partial<Task>) => api.post<ApiResponse<Task>>('/tasks', task),
    updateTask: (id: number, task: Partial<Task>) => api.put<ApiResponse<Task>>(`/tasks/${id}`, task),
    deleteTask: (id: number) => api.delete(`/tasks/${id}`),
    completeTask: (id: number) => api.post<ApiResponse<Task>>(`/tasks/${id}/complete`),
    uncompleteTask: (id: number) => api.post<ApiResponse<Task>>(`/tasks/${id}/uncomplete`),
};

// Transactions API
export const transactionsApi = {
    getTransactions: () => api.get<ApiResponse<Transaction[]>>('/transactions'),
    getTransaction: (id: number) => api.get<ApiResponse<Transaction>>(`/transactions/${id}`),
    createTransaction: (transaction: Partial<Transaction>) => 
        api.post<ApiResponse<Transaction>>('/transactions', transaction),
    updateTransaction: (id: number, transaction: Partial<Transaction>) =>
        api.put<ApiResponse<Transaction>>(`/transactions/${id}`, transaction),
    deleteTransaction: (id: number) => api.delete(`/transactions/${id}`),
};

// Auth API
export const authApi = {
    login: (email: string, password: string) => 
        api.post<ApiResponse<{ token: string; user: User }>>('/auth/login', { email, password }),
    register: (userData: Partial<User>) => 
        api.post<ApiResponse<User>>('/auth/register', userData),
    getCurrentUser: () => api.get<ApiResponse<User>>('/auth/me'),
};

export const getActiveTransactions = async () => {
    const response = await api.get('/transactions?status=active');
    return response.data;
};

export const getTasks = async (params = {}) => {
    const response = await api.get('/tasks', { params });
    return response.data;
};

export const getRecentActivity = async () => {
    const response = await api.get('/activities/recent');
    return response.data;
};

export default api; 