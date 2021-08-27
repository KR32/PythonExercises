-- select count(*) from users
-- select count(*) from candidates
-- 670 users 
-- 624 candidates
-- 7504 candidate_uid
--  8644 user_id

-- final test
-- user 9094 candidate 7954

-- select user_id,
--     candidate_uid
-- from candidates order by candidate_uid desc


-- select customer.customer_uid,
--     customer.customer_type_id,
--     customer_type.customer_type
-- from customer
--     join customer_type on customer.customer_type_id = customer_type.customer_type_id 



    -- select * from customer_organisations
    -- select customer_organisations.customer_uid,
    --     customer_organisations.organisation_id,
    --     organisations.parent_org_id,
    --     organisations.is_parent,
    --     customer_organisation_locations.path_acronym
    -- from customer_organisations
    --     join organisations on customer_organisations.organisation_id = organisations.organisation_id
    --     join customer_organisation_locations on customer_organisation_locations.customer_organisation_id = customer_organisations.id 
    -- order by organisations.parent_org_id
    -- order by customer_organisations.customer_uid