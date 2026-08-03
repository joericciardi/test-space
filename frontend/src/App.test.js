import { render, screen } from '@testing-library/react';
import App from './App';

test('renders login link in nav', () => {
  render(<App />);
  const linkElements = screen.getAllByText(/Login/i);
  expect(linkElements.length).toBeGreaterThan(0);
});
