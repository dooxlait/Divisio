
```
Divisio
├─ .devcontainer
│  └─ devcontainer.json
├─ .dockerignore
├─ BACKEND
│  ├─ app
│  │  ├─ common
│  │  │  ├─ base
│  │  │  │  ├─ base_model.py
│  │  │  │  └─ base_schema.py
│  │  │  ├─ helper
│  │  │  │  ├─ excel_helper.py
│  │  │  │  ├─ parse_helper.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ response
│  │  │  │  ├─ response.py
│  │  │  │  └─ response_schema.py
│  │  │  └─ utils.py
│  │  │     └─ normalize_date.py
│  │  ├─ core
│  │  │  ├─ config.py
│  │  │  ├─ cors.py
│  │  │  ├─ extensions.py
│  │  │  └─ security.py
│  │  ├─ modules
│  │  │  ├─ API
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ healthcheck_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ articles
│  │  │  │  ├─ models
│  │  │  │  │  ├─ articles.py
│  │  │  │  │  ├─ caracteristique_article.py
│  │  │  │  │  ├─ categories.py
│  │  │  │  │  ├─ composition.py
│  │  │  │  │  ├─ fournisseur.py
│  │  │  │  │  ├─ marques.py
│  │  │  │  │  ├─ mouvement_stock.py
│  │  │  │  │  ├─ palettisation.py
│  │  │  │  │  ├─ stock.py
│  │  │  │  │  ├─ unite.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ article_composition_routes.py
│  │  │  │  │  ├─ article_routes.py
│  │  │  │  │  ├─ category_routes.py
│  │  │  │  │  ├─ fournisseur_routes.py
│  │  │  │  │  ├─ marque_routes.py
│  │  │  │  │  ├─ mouvement_stock_routes.py
│  │  │  │  │  ├─ stock_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ schemas
│  │  │  │  │  ├─ article
│  │  │  │  │  │  ├─ article_read_schema.py
│  │  │  │  │  │  ├─ article_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ caracteristique_article
│  │  │  │  │  │  ├─ caracteristique_article_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ category
│  │  │  │  │  │  ├─ category_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ composition
│  │  │  │  │  │  ├─ composition_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ fournisseur
│  │  │  │  │  │  ├─ fournisseur_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ marques
│  │  │  │  │  │  ├─ marque_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ mouvement_stock
│  │  │  │  │  │  ├─ mouvement_stock_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ palettisation
│  │  │  │  │  │  ├─ palletisation_read_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ stock
│  │  │  │  │  │  ├─ stock_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ unite
│  │  │  │  │  │  ├─ unite_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ services
│  │  │  │  │  ├─ article_composition.py
│  │  │  │  │  ├─ article_service.py
│  │  │  │  │  ├─ category_service.py
│  │  │  │  │  ├─ fournisseur_service.py
│  │  │  │  │  ├─ marque_service.py
│  │  │  │  │  ├─ stock_service.py
│  │  │  │  │  ├─ unite_service.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ factory
│  │  │  │  ├─ models
│  │  │  │  │  ├─ division.py
│  │  │  │  │  ├─ division_certification.py
│  │  │  │  │  ├─ site.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ division_routes.py
│  │  │  │  │  ├─ site_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ schemas
│  │  │  │  │  ├─ division
│  │  │  │  │  │  ├─ DivisionCreateSchema.py
│  │  │  │  │  │  ├─ DivisionSchema.py
│  │  │  │  │  │  ├─ DivisionUpdateSchema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ site
│  │  │  │  │  │  ├─ SiteCreateSchema.py
│  │  │  │  │  │  ├─ SiteSchema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ services
│  │  │  │  │  ├─ division_service.py
│  │  │  │  │  ├─ site_service.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ hr
│  │  │  │  ├─ models
│  │  │  │  │  ├─ certification.py
│  │  │  │  │  ├─ certification_employee.py
│  │  │  │  │  ├─ division_employee.py
│  │  │  │  │  ├─ employee.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ divisionemployee_routes.py
│  │  │  │  │  ├─ employee_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ schemas
│  │  │  │  │  ├─ division_employee
│  │  │  │  │  │  ├─ DivisionEmployeeCreateSchema.py
│  │  │  │  │  │  ├─ DivisionEmployeeSchema.py
│  │  │  │  │  │  ├─ DivisionEmployeeUpdateSchema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ employee
│  │  │  │  │  │  ├─ EmployeeCreateSchema.py
│  │  │  │  │  │  ├─ EmployeeSchema.py
│  │  │  │  │  │  ├─ EmployeeUpdateSchema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ services
│  │  │  │  │  ├─ divisionsemployees_service.py
│  │  │  │  │  ├─ employee_services.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ inventory
│  │  │  │  ├─ models
│  │  │  │  │  ├─ article.py
│  │  │  │  │  ├─ inventory_balance.py
│  │  │  │  │  ├─ inventory_transaction.py
│  │  │  │  │  ├─ location.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ machine
│  │  │  │  ├─ models
│  │  │  │  │  ├─ machine.py
│  │  │  │  │  ├─ machine_document.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ machine_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ schemas
│  │  │  │  │  ├─ machine
│  │  │  │  │  │  ├─ MachineCreateSchema.py
│  │  │  │  │  │  ├─ MachineSchema.py
│  │  │  │  │  │  ├─ MachineUpdateSchema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  ├─ machine_document
│  │  │  │  │  │  ├─ MachineDocumentCreateSchema.py
│  │  │  │  │  │  ├─ MachineDocumentSchema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ services
│  │  │  │  │  ├─ machine_service.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ maintenance
│  │  │  │  ├─ models
│  │  │  │  │  ├─ maintenance_request.py
│  │  │  │  │  ├─ spare.py
│  │  │  │  │  ├─ work_order.py
│  │  │  │  │  ├─ work_order_part.py
│  │  │  │  │  ├─ work_order_task.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ planning
│  │  │  │  ├─ models
│  │  │  │  │  ├─ production_schedule.py
│  │  │  │  │  ├─ schedule_allocation.py
│  │  │  │  │  ├─ shift.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ process
│  │  │  │  ├─ models
│  │  │  │  │  ├─ process.py
│  │  │  │  │  ├─ process_machine.py
│  │  │  │  │  ├─ process_step.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ production
│  │  │  │  ├─ models
│  │  │  │  │  ├─ production_material.py
│  │  │  │  │  ├─ production_order.py
│  │  │  │  │  ├─ production_output.py
│  │  │  │  │  ├─ production_recipe.py
│  │  │  │  │  ├─ production_task.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ production_order_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ schemas
│  │  │  │  │  ├─ production_order
│  │  │  │  │  │  ├─ production_order_create_schema.py
│  │  │  │  │  │  ├─ production_order_light_schema.py
│  │  │  │  │  │  ├─ production_order_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ services
│  │  │  │  │  ├─ production_order_service.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ quality
│  │  │  │  ├─ models
│  │  │  │  │  ├─ capa_action.py
│  │  │  │  │  ├─ non_conformity.py
│  │  │  │  │  ├─ quality_check.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ statistique
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ statistique_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ service
│  │  │  │  │  └─ statistique_service.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ Divisio_workspace.code-workspace
│  ├─ Dockerfile
│  ├─ docs
│  │  └─ architecture
│  │     ├─ architecture.txt
│  │     └─ Démarrage.txt
│  ├─ global_reqs.txt
│  ├─ launcher
│  │  ├─ initial_migration.py
│  │  ├─ launcher_service.py
│  │  └─ __init__.py
│  ├─ launcher.ps1
│  ├─ migrations
│  │  ├─ alembic.ini
│  │  ├─ env.py
│  │  ├─ README
│  │  ├─ script.py.mako
│  │  └─ versions
│  │     └─ 05917e9f1bb0_auto_migration.py
│  ├─ requirements.txt
│  ├─ run.py
│  └─ starter
│     ├─ clean.bat
│     ├─ cold_start.bat
│     └─ hot_start.bat
├─ Divisio_workspace.code-workspace
├─ docker-compose.yml
├─ README.md
└─ RESSOURCES
   ├─ DB_ARTICLES.xlsx
   ├─ DLC-DGR PRODUITS Toutes Marques.xlsx
   ├─ EMBALLAGES PAR PRODUITS TTES MARQUES.xlsx
   ├─ Stats_multicrit_20251106_104342.xls
   ├─ STOCK PANDA.xlsx
   └─ STOCK.xlsx

```