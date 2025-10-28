
```
Divisio
├─ .dockerignore
├─ BACKEND
│  ├─ app
│  │  ├─ common
│  │  │  ├─ base
│  │  │  │  ├─ base_model.py
│  │  │  │  └─ base_schema.py
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
│  │  │  │  │  ├─ categories.py
│  │  │  │  │  ├─ composition.py
│  │  │  │  │  ├─ fournisseur.py
│  │  │  │  │  ├─ marques.py
│  │  │  │  │  ├─ unite.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ routes
│  │  │  │  │  ├─ article_routes.py
│  │  │  │  │  ├─ category_routes.py
│  │  │  │  │  ├─ marque_routes.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ schemas
│  │  │  │  │  ├─ article
│  │  │  │  │  │  ├─ article_schema.py
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
│  │  │  │  │  ├─ unite
│  │  │  │  │  │  ├─ unite_schema.py
│  │  │  │  │  │  └─ __init__.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  ├─ services
│  │  │  │  │  ├─ article_composition.py
│  │  │  │  │  ├─ article_service.py
│  │  │  │  │  ├─ category_service.py
│  │  │  │  │  ├─ marque_service.py
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
│  │  │  │  │  ├─ production_task.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ quality
│  │  │  │  ├─ models
│  │  │  │  │  ├─ capa_action.py
│  │  │  │  │  ├─ non_conformity.py
│  │  │  │  │  ├─ quality_check.py
│  │  │  │  │  └─ __init__.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ RESSOURCES
│  │  │  │  └─ Export
│  │  │  │     ├─ exported_articles_20251024_142613.xlsx
│  │  │  │     ├─ exported_articles_20251024_142755.xlsx
│  │  │  │     └─ exported_articles_20251027_115328.xlsx
│  │  │  └─ __init__.py
│  │  └─ __init__.py
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
│  │     └─ 7e039ab8020e_auto_migration.py
│  ├─ requirements.txt
│  ├─ run.py
│  └─ starter
│     ├─ clean.bat
│     ├─ cold_start.bat
│     └─ hot_start.bat
├─ docker-compose.yml
├─ FRONTEND
│  ├─ docs
│  │  ├─ webapparchitecture.txt
│  │  └─ wireframe.txt
│  └─ webapp
│     ├─ Dockerfile
│     ├─ eslint.config.mjs
│     ├─ jsconfig.json
│     ├─ next.config.mjs
│     ├─ package.json
│     ├─ public
│     │  ├─ file.svg
│     │  ├─ globe.svg
│     │  ├─ morice_sas_logo-removedbg.png
│     │  ├─ morice_sas_logo.jpg
│     │  ├─ next.svg
│     │  ├─ vercel.svg
│     │  └─ window.svg
│     ├─ README.md
│     └─ src
│        ├─ app
│        │  ├─ (auth)
│        │  │  └─ identification
│        │  │     ├─ layout.jsx
│        │  │     ├─ layout.module.css
│        │  │     ├─ page.jsx
│        │  │     └─ page.module.css
│        │  ├─ (main)
│        │  │  ├─ dashboard
│        │  │  │  ├─ page.jsx
│        │  │  │  └─ page.module.css
│        │  │  ├─ factory
│        │  │  │  ├─ divisions
│        │  │  │  │  ├─ creer-division
│        │  │  │  │  │  ├─ page.jsx
│        │  │  │  │  │  └─ page.module.css
│        │  │  │  │  ├─ layout.jsx
│        │  │  │  │  ├─ layout.module.css
│        │  │  │  │  ├─ lire-division
│        │  │  │  │  │  ├─ layout.jsx
│        │  │  │  │  │  ├─ layout.module.css
│        │  │  │  │  │  ├─ page.jsx
│        │  │  │  │  │  └─ page.module.css
│        │  │  │  │  ├─ page.jsx
│        │  │  │  │  └─ page.module.css
│        │  │  │  ├─ layout.jsx
│        │  │  │  ├─ layout.module.css
│        │  │  │  └─ site
│        │  │  │     ├─ creer-site
│        │  │  │     │  ├─ layout.jsx
│        │  │  │     │  ├─ layout.module.css
│        │  │  │     │  ├─ page.jsx
│        │  │  │     │  └─ page.module.css
│        │  │  │     ├─ layout.jsx
│        │  │  │     ├─ layout.module.css
│        │  │  │     ├─ lire-site
│        │  │  │     │  ├─ page.jsx
│        │  │  │     │  └─ page.module.css
│        │  │  │     ├─ page.jsx
│        │  │  │     └─ page.module.css
│        │  │  ├─ layout.jsx
│        │  │  ├─ layout.module.css
│        │  │  ├─ loading.jsx
│        │  │  └─ products
│        │  │     ├─ layout.jsx
│        │  │     ├─ layout.module.css
│        │  │     ├─ packaging-formats
│        │  │     │  ├─ page.jsx
│        │  │     │  └─ page.module.css
│        │  │     ├─ pallets
│        │  │     │  ├─ page.jsx
│        │  │     │  └─ page.module.css
│        │  │     ├─ raw-material
│        │  │     │  ├─ create
│        │  │     │  │  ├─ page.jsx
│        │  │     │  │  └─ page.module.css
│        │  │     │  ├─ page.jsx
│        │  │     │  ├─ page.module.css
│        │  │     │  └─ read
│        │  │     │     ├─ page.jsx
│        │  │     │     └─ page.module.css
│        │  │     ├─ type-products
│        │  │     │  ├─ page.jsx
│        │  │     │  └─ page.module.css
│        │  │     └─ variants-products
│        │  │        ├─ page.jsx
│        │  │        └─ page.module.css
│        │  ├─ favicon.ico
│        │  ├─ globals.css
│        │  ├─ layout.jsx
│        │  ├─ page.jsx
│        │  └─ page.module.css
│        ├─ components
│        │  ├─ auth
│        │  │  ├─ loginForm
│        │  │  │  ├─ LoginForm.jsx
│        │  │  │  └─ LoginForm.module.css
│        │  │  └─ logo
│        │  │     ├─ logo.jsx
│        │  │     └─ logo.module.css
│        │  ├─ cards
│        │  │  └─ mini-card
│        │  │     ├─ minicard.jsx
│        │  │     └─ minicard.module.css
│        │  ├─ feedback
│        │  │  └─ splashscreen
│        │  │     ├─ SplashScreen.jsx
│        │  │     └─ SplashScreen.module.css
│        │  ├─ form
│        │  │  ├─ SiteForm
│        │  │  │  ├─ SiteForm.jsx
│        │  │  │  └─ SiteForm.module.css
│        │  │  └─ SiteSelect
│        │  │     ├─ SiteSelect.jsx
│        │  │     └─ SiteSelect.module.css
│        │  ├─ layout
│        │  │  ├─ Header
│        │  │  │  ├─ Header.jsx
│        │  │  │  └─ Header.module.css
│        │  │  ├─ Logo
│        │  │  │  ├─ logo.jsx
│        │  │  │  └─ logo.module.css
│        │  │  └─ Sidebar
│        │  │     ├─ Sidebar.jsx
│        │  │     └─ Sidebar.module.css
│        │  └─ ui
│        │     ├─ Button
│        │     │  ├─ ActionButton.jsx
│        │     │  └─ LoadingNavigateButton.jsx
│        │     ├─ Checkbox.jsx
│        │     ├─ Form.jsx
│        │     ├─ HierarchyBuilder
│        │     │  ├─ HierarchyBuilder.jsx
│        │     │  ├─ HierarchyBuilder.module.css
│        │     │  ├─ ParentTree.jsx
│        │     │  ├─ ParentTree.module.css
│        │     │  ├─ TreeNode.jsx
│        │     │  └─ TreeNode.module.css
│        │     ├─ InputText.jsx
│        │     ├─ Select.jsx
│        │     ├─ Spinner.jsx
│        │     └─ TextArea.jsx
│        ├─ config
│        │  ├─ servicechoice.config.js
│        │  └─ sidebar.config.js
│        ├─ context
│        │  └─ SessionContext.jsx
│        ├─ helpers
│        │  └─ buildHierarchy.js
│        ├─ hooks
│        │  ├─ useApi.js
│        │  ├─ useApiCheck.js
│        │  ├─ useRequest.js
│        │  └─ useSplash.js
│        ├─ services
│        │  └─ AxiosInstance.js
│        └─ utils
│           └─ string.js
└─ RESSOURCES
   ├─ DB_ARTICLES.xlsx
   ├─ EMBALLAGES PAR PRODUITS TTES MARQUES.xlsx
   ├─ ~$DB_ARTICLES.xlsx
   └─ ~$EMBALLAGES PAR PRODUITS TTES MARQUES.xlsx

```