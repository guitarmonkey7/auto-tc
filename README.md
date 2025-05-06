# Real Estate Transaction Coordination Automation

An automated system for managing real estate transactions, including PDF data extraction, workflow automation, and client communication.

## Features

- PDF data extraction from real estate documents
- Automated workflow management
- Email and calendar integration
- Vendor management
- Transaction tracking and management

## Project Structure

```
.
├── backend/                 # FastAPI backend
│   ├── app/                # Application code
│   │   ├── api/           # API routes
│   │   ├── core/          # Core functionality
│   │   ├── models/        # Database models
│   │   ├── schemas/       # Pydantic schemas
│   │   └── services/      # Business logic
│   └── tests/             # Backend tests
├── frontend/               # React frontend
│   ├── src/               # Source code
│   └── public/            # Static assets
└── docs/                  # Documentation
```

## %%% THIS SECTION IS UNDER CONSTRUCTION AND MAY CHANGE SIGNIFICANTLY %%%
## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the backend directory with:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
ASANA_ACCESS_TOKEN=your_asana_token
```

4. Initialize the database:
```bash
cd backend
alembic upgrade head
```

5. Start the development server:
```bash
uvicorn app.main:app --reload
```
## %%% END UNDER CONSTRUCTION SECTION %%%

## Development Roadmap

1. Phase 1: Foundation
   - User authentication
   - Basic transaction management
   - PDF upload and storage
   - Dashboard

2. Phase 2: PDF Processing
   - Data extraction
   - OCR integration
   - Validation interface

3. Phase 3: Workflow Automation
   - Email automation
   - Calendar integration
   - Asana integration

4. Phase 4: Enhanced Features
   - Advanced search
   - Document repository
   - Reporting
   - Mobile responsiveness 


## Dev Notes

In order to use pdf2image to convert a pdf into an image for markup, Popplar must be installed.
This process varies by installation. See the information here: https://pdf2image.readthedocs.io/en/latest/installation.html#installing-poppler
This will need to be added to the Docker Container for this to run as a containerized service