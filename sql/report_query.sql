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
CustomerSummary AS (
    SELECT
        f.branch,
        p.product_line,
        c.gender,
        COUNT(c.customer_id) AS customer_count,
        SUM(f.total_amount) AS total_revenue_by_gender
    FROM Sales f
    JOIN Product p ON f.product_id = p.product_id
    JOIN Customer c ON f.customer_id = c.customer_id
    GROUP BY f.branch, p.product_line, c.gender
),
RankedRevenue AS (
    SELECT
        r.branch,
        r.product_line,
        r.total_revenue,
        r.branch_total_revenue,
        ROUND((r.total_revenue * 100.0 / r.branch_total_revenue), 2) AS revenue_percentage,
        RANK() OVER (PARTITION BY r.branch ORDER BY r.total_revenue DESC) AS revenue_rank
    FROM RevenueSummary r
)
SELECT
    r.branch,
    r.product_line,
    r.total_revenue,
    r.revenue_percentage,
    r.revenue_rank,
    cs.gender,
    cs.customer_count,
    cs.total_revenue_by_gender
FROM RankedRevenue r
LEFT JOIN CustomerSummary cs 
    ON r.branch = cs.branch AND r.product_line = cs.product_line
ORDER BY r.branch, r.revenue_rank;