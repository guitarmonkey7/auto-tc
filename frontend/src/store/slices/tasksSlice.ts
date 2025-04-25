import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { Task } from '../../types';
import { tasksApi } from '../../services/api';

interface TasksState {
    tasks: Task[];
    loading: boolean;
    error: string | null;
}

const initialState: TasksState = {
    tasks: [],
    loading: false,
    error: null,
};

export const fetchTasks = createAsyncThunk(
    'tasks/fetchTasks',
    async () => {
        const response = await tasksApi.getTasks();
        return response.data.data;
    }
);

export const createTask = createAsyncThunk(
    'tasks/createTask',
    async (task: Partial<Task>) => {
        const response = await tasksApi.createTask(task);
        return response.data.data;
    }
);

export const updateTask = createAsyncThunk(
    'tasks/updateTask',
    async ({ id, task }: { id: number; task: Partial<Task> }) => {
        const response = await tasksApi.updateTask(id, task);
        return response.data.data;
    }
);

export const deleteTask = createAsyncThunk(
    'tasks/deleteTask',
    async (id: number) => {
        await tasksApi.deleteTask(id);
        return id;
    }
);

const tasksSlice = createSlice({
    name: 'tasks',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchTasks.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(fetchTasks.fulfilled, (state, action) => {
                state.loading = false;
                state.tasks = action.payload;
            })
            .addCase(fetchTasks.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message || 'Failed to fetch tasks';
            })
            .addCase(createTask.fulfilled, (state, action) => {
                state.tasks.push(action.payload);
            })
            .addCase(updateTask.fulfilled, (state, action) => {
                const index = state.tasks.findIndex(task => task.id === action.payload.id);
                if (index !== -1) {
                    state.tasks[index] = action.payload;
                }
            })
            .addCase(deleteTask.fulfilled, (state, action) => {
                state.tasks = state.tasks.filter(task => task.id !== action.payload);
            });
    },
});

export default tasksSlice.reducer; 