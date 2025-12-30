import apiClient from './api-client';

export interface UserCredentials {
  username: string;
  password: string;
}

export interface UserRegistration {
  username: string;
  password: string;
  email?: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface User {
  id: number;
  username: string;
  email: string | null;
  is_active: boolean;
  created_at: number;
}

export const login = async (credentials: UserCredentials): Promise<AuthResponse> => {
  const response = await apiClient.post('/auth/login', credentials);
  return response.data;
};

export const register = async (userData: UserRegistration): Promise<User> => {
  const response = await apiClient.post('/auth/register', userData);
  return response.data;
};

export const getCurrentUser = async (token: string): Promise<User> => {
  const response = await apiClient.get('/auth/me', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};
