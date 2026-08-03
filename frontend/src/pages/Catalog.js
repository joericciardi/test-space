import React, { useEffect, useState } from 'react';
import { fetchCatalog } from '../services/api';

function Catalog() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const loadCatalog = async () => {
      try {
        const res = await fetchCatalog();
        setItems(res.data);
      } catch (err) {
        setError('Failed to load catalog');
      }
    };
    loadCatalog();
  }, []);

  return (
    <div>
      <h2>Clothing Catalog</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}

      <div style={{ display: 'grid', gap: '20px' }}>
        {items.map((item, idx) => (
          <div key={idx} style={{ border: '1px solid #ccc', padding: '15px' }}>
            <h3>{item.type}</h3>
            <h4>How to measure:</h4>
            <ul>
              {Object.entries(item.how_to_measure).map(([key, desc]) => (
                <li key={key}><strong>{key}:</strong> {desc}</li>
              ))}
            </ul>
            <h4>Available Sizes:</h4>
            <div style={{ display: 'flex', gap: '10px', overflowX: 'auto' }}>
              <table border="1" cellPadding="5">
                <thead>
                  <tr>
                    <th>Dimension</th>
                    {Object.keys(Object.values(item.sizes)[0]).map(size => (
                      <th key={size}>{size}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(item.sizes).map(([dim, sizesObj]) => (
                    <tr key={dim}>
                      <td><strong>{dim}</strong></td>
                      {Object.values(sizesObj).map((val, i) => (
                        <td key={i}>{val}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <button style={{ marginTop: '10px' }}>Try On Visually</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Catalog;
