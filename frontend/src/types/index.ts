// Task Types
export interface Task {
    id: number;
    title: string;
    description: string;
    completed: boolean;
    completed_at?: string;
    created_at: string;
    transaction_id?: number;
    created_by_id: number;
}

// Transaction Types
export interface Transaction {
    id: number;
    transaction_id: string;
    property_address: string;
    client_name: string;
    status: 'active' | 'archived';
    created_at: string;
    updated_at: string;
}

// User Types
export interface User {
    id: number;
    email: string;
    full_name: string;
    role: string;
}

// API Response Types
export interface ApiResponse<T> {
    data: T;
    message?: string;
    error?: string;
} 