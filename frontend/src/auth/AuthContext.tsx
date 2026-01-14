import { createContext, useContext, useState } from "react";
import type { ReactNode } from "react";

import api from "../api/axios";
import type { TokenResponse } from "../types/models";

interface AuthContextType {
  user: string | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<string | null>(null);

  const login = async (email: string, password: string) => {
    const res = await api.post<TokenResponse>("/auth/login", {
      email,
      password,
    });
    localStorage.setItem("access_token", res.data.access_token);
    setUser(email);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// eslint-disable-next-line react-refresh/only-export-components
export const useAuth = (): AuthContextType => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
};
