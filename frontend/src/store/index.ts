import { configureStore } from '@reduxjs/toolkit';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';
import tasksReducer from './slices/tasksSlice';
import transactionsReducer from './slices/transactionsSlice';
import authReducer from './slices/authSlice';

export const store = configureStore({
    reducer: {
        tasks: tasksReducer,
        transactions: transactionsReducer,
        auth: authReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector; 