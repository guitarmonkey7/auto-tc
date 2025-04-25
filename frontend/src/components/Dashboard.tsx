import React, { useEffect, useState } from 'react';
import {
    Grid,
    Paper,
    Typography,
    Box,
    List,
    ListItem,
    ListItemText,
    ListItemIcon,
    CircularProgress,
} from '@mui/material';
import {
    Assignment as AssignmentIcon,
    CheckCircle as CheckCircleIcon,
    Warning as WarningIcon,
} from '@mui/icons-material';
import { getActiveTransactions, getTasks, getRecentActivity } from '../services/api';

interface DashboardStats {
    activeTransactions: number;
    completedTasks: number;
    pendingTasks: number;
}

interface Activity {
    id: number;
    type: string;
    text: string;
    time: string;
}

const Dashboard: React.FC = () => {
    const [stats, setStats] = useState<DashboardStats>({
        activeTransactions: 0,
        completedTasks: 0,
        pendingTasks: 0,
    });
    const [recentActivity, setRecentActivity] = useState<Activity[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchDashboardData = async () => {
            try {
                setLoading(true);
                const [transactions, tasks, activities] = await Promise.all([
                    getActiveTransactions(),
                    getTasks(),
                    getRecentActivity(),
                ]);

                setStats({
                    activeTransactions: transactions.length,
                    completedTasks: tasks.filter((task: any) => task.completed).length,
                    pendingTasks: tasks.filter((task: any) => !task.completed).length,
                });

                setRecentActivity(activities);
                setError(null);
            } catch (err) {
                setError('Failed to load dashboard data');
                console.error('Error fetching dashboard data:', err);
            } finally {
                setLoading(false);
            }
        };

        fetchDashboardData();
    }, []);

    if (loading) {
        return (
            <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
                <CircularProgress />
            </Box>
        );
    }

    if (error) {
        return (
            <Box sx={{ p: 3 }}>
                <Typography color="error">{error}</Typography>
            </Box>
        );
    }

    return (
        <Box sx={{ flexGrow: 1, p: 3 }}>
            <Typography variant="h4" gutterBottom>
                Dashboard
            </Typography>
            
            <Grid container spacing={3}>
                {/* Statistics Cards */}
                <Grid container item xs={12} md={4}>
                    <Paper sx={{ p: 2, width: '100%' }}>
                        <Typography variant="h6" gutterBottom>
                            Active Transactions
                        </Typography>
                        <Typography variant="h3">
                            {stats.activeTransactions}
                        </Typography>
                    </Paper>
                </Grid>
                <Grid container item xs={12} md={4}>
                    <Paper sx={{ p: 2, width: '100%' }}>
                        <Typography variant="h6" gutterBottom>
                            Completed Tasks
                        </Typography>
                        <Typography variant="h3">
                            {stats.completedTasks}
                        </Typography>
                    </Paper>
                </Grid>
                <Grid container item xs={12} md={4}>
                    <Paper sx={{ p: 2, width: '100%' }}>
                        <Typography variant="h6" gutterBottom>
                            Pending Tasks
                        </Typography>
                        <Typography variant="h3">
                            {stats.pendingTasks}
                        </Typography>
                    </Paper>
                </Grid>

                {/* Recent Activity */}
                <Grid container item xs={12}>
                    <Paper sx={{ p: 2, width: '100%' }}>
                        <Typography variant="h6" gutterBottom>
                            Recent Activity
                        </Typography>
                        <List>
                            {recentActivity.map((activity) => (
                                <ListItem key={activity.id}>
                                    <ListItemIcon>
                                        {activity.type === 'transaction' ? (
                                            <AssignmentIcon />
                                        ) : activity.type === 'task' ? (
                                            <CheckCircleIcon />
                                        ) : (
                                            <WarningIcon />
                                        )}
                                    </ListItemIcon>
                                    <ListItemText
                                        primary={activity.text}
                                        secondary={activity.time}
                                    />
                                </ListItem>
                            ))}
                        </List>
                    </Paper>
                </Grid>
            </Grid>
        </Box>
    );
};

export default Dashboard; 