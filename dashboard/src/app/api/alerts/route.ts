import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET() {
    try {
        const filePath = path.join(process.cwd(), '..', 'shared', 'alerts.json');

        if (!fs.existsSync(filePath)) {
            return NextResponse.json([]);
        }

        const fileContent = fs.readFileSync(filePath, 'utf8');
        const data = JSON.parse(fileContent);

        return NextResponse.json(data);
    } catch (error) {
        return NextResponse.json({ error: "Failed to load alerts" }, { status: 500 });
    }
}