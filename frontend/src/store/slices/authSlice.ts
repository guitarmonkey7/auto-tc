import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { User } from '../../types';
import { authApi } from '../../services/api';

interface AuthState {
    user: User | null;
    token: string | null;
    loading: boolean;
    error: string | null;
}

const initialState: AuthState = {
    user: null,
    token: localStorage.getItem('token'),
    loading: false,
    error: null,
};

export const login = createAsyncThunk(
    'auth/login',
    async ({ email, password }: { email: string; password: string }) => {
        const response = await authApi.login(email, password);
        localStorage.setItem('token', response.data.data.token);
        return response.data.data;
    }
);

export const register = createAsyncThunk(
    'auth/register',
    async (userData: Partial<User>) => {
        const response = await authApi.register(userData);
        return response.data.data;
    }
);

export const getCurrentUser = createAsyncThunk(
    'auth/getCurrentUser',
    async () => {
        const response = await authApi.getCurrentUser();
        return response.data.data;
    }
);

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        logout: (state) => {
            state.user = null;
            state.token = null;
            localStorage.removeItem('token');
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(login.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(login.fulfilled, (state, action) => {
                state.loading = false;
                state.user = action.payload.user;
                state.token = action.payload.token;
            })
            .addCase(login.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message || 'Login failed';
            })
            .addCase(register.fulfilled, (state, action) => {
                state.user = action.payload;
            })
            .addCase(getCurrentUser.fulfilled, (state, action) => {
                state.user = action.payload;
            });
    },
});

export const { logout } = authSlice.actions;
export default authSlice.reducer; 