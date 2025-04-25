import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { Transaction } from '../../types';
import { transactionsApi } from '../../services/api';

interface TransactionsState {
    transactions: Transaction[];
    loading: boolean;
    error: string | null;
}

const initialState: TransactionsState = {
    transactions: [],
    loading: false,
    error: null,
};

export const fetchTransactions = createAsyncThunk(
    'transactions/fetchTransactions',
    async () => {
        const response = await transactionsApi.getTransactions();
        return response.data.data;
    }
);

export const createTransaction = createAsyncThunk(
    'transactions/createTransaction',
    async (transaction: Partial<Transaction>) => {
        const response = await transactionsApi.createTransaction(transaction);
        return response.data.data;
    }
);

export const updateTransaction = createAsyncThunk(
    'transactions/updateTransaction',
    async ({ id, transaction }: { id: number; transaction: Partial<Transaction> }) => {
        const response = await transactionsApi.updateTransaction(id, transaction);
        return response.data.data;
    }
);

export const deleteTransaction = createAsyncThunk(
    'transactions/deleteTransaction',
    async (id: number) => {
        await transactionsApi.deleteTransaction(id);
        return id;
    }
);

const transactionsSlice = createSlice({
    name: 'transactions',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchTransactions.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(fetchTransactions.fulfilled, (state, action) => {
                state.loading = false;
                state.transactions = action.payload;
            })
            .addCase(fetchTransactions.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message || 'Failed to fetch transactions';
            })
            .addCase(createTransaction.fulfilled, (state, action) => {
                state.transactions.push(action.payload);
            })
            .addCase(updateTransaction.fulfilled, (state, action) => {
                const index = state.transactions.findIndex(t => t.id === action.payload.id);
                if (index !== -1) {
                    state.transactions[index] = action.payload;
                }
            })
            .addCase(deleteTransaction.fulfilled, (state, action) => {
                state.transactions = state.transactions.filter(t => t.id !== action.payload);
            });
    },
});

export default transactionsSlice.reducer; 