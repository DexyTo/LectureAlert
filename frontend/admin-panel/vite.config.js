import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import path from 'path'; // Добавьте этот импорт

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      '@locationImages': path.resolve(__dirname, '../../location_images')
    }
  }
});