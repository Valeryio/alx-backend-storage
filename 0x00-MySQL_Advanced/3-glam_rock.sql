-- glam rock script
SELECT band_name, formed, split, IFNULL(split, 2022) - formed as lifespan FROM metal_bands where
style LIKE '%Glam rock%';
