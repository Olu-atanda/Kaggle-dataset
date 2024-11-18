WITH RevenueSummary AS (
    SELECT 
        f.branch,
        p.product_line,
        SUM(f.total_amount) AS total_revenue,
        SUM(SUM(f.total_amount)) OVER (PARTITION BY f.branch) AS branch_total_revenue
    FROM Sales f
    JOIN Product p ON f.product_id = p.product_id
    GROUP BY f.branch, p.product_line
),
RankedRevenue AS (
    SELECT
        branch,
        product_line,
        total_revenue,
        branch_total_revenue,
        ROUND((total_revenue * 100.0 / branch_total_revenue), 2) AS revenue_percentage,
        RANK() OVER (PARTITION BY branch ORDER BY total_revenue DESC) AS revenue_rank
    FROM RevenueSummary
)
SELECT
    branch,
    product_line,
    total_revenue,
    revenue_percentage,
    revenue_rank
FROM RankedRevenue
ORDER BY branch, revenue_rank;