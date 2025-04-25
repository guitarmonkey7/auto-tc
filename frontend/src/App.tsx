import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { store } from './store';
import MainLayout from './layouts/MainLayout';
import Dashboard from './components/Dashboard';

// Create a theme instance
const theme = createTheme({
    palette: {
        primary: {
            main: '#1976d2',
        },
        secondary: {
            main: '#dc004e',
        },
    },
});

function App() {
    return (
        <Provider store={store}>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <Router>
                    <MainLayout>
                        <Routes>
                            <Route path="/" element={<Dashboard />} />
                            <Route path="/transactions" element={<div>Transactions</div>} />
                            <Route path="/tasks" element={<div>Tasks</div>} />
                            <Route path="/users" element={<div>Users</div>} />
                            <Route path="/settings" element={<div>Settings</div>} />
                        </Routes>
                    </MainLayout>
                </Router>
            </ThemeProvider>
        </Provider>
    );
}

export default App;
