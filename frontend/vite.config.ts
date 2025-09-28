import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import svgr from 'vite-plugin-svgr';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), svgr()],
  resolve: {
    dedupe: ['react', 'react-dom'], // prevents duplicate copies from deps
  },
  server: {
    proxy: {
      // Anything starting with /api will be proxied to the FastAPI backend
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
})
