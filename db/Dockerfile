FROM postgres:14

COPY db/init.sql db/migration.sh /migrate/
RUN chmod +x migrate/migration.sh
ENTRYPOINT ["migrate/migration.sh"]