CREATE TABLE IF NOT EXISTS Sales (
    invoice_id TEXT PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    date DATE NOT NULL,
    branch TEXT NOT NULL,
    city TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    total_amount REAL NOT NULL,
    payment_method TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
    FOREIGN KEY (product_id) REFERENCES Product (product_id)
);
