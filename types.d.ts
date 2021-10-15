declare global {
  namespace NodeJS {
    interface ProcessEnv {
      DATABASE_URL: string;
      NODE_ENV: "development" | "production";
      JWT_TOKEN: string;
    }
  }
}
export {};
